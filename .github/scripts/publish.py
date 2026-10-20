import hashlib,json,pathlib,re,subprocess,zipfile
root=pathlib.Path(__file__).resolve().parents[2]
for folder in sorted((root/'releases').iterdir(),key=lambda p:tuple(map(int,p.name.split('.')))):
    if not re.fullmatch(r'\d+\.\d+\.\d+',folder.name): raise RuntimeError('Unexpected release directory')
    manifest=folder/'blueprint-release.json';signature=folder/'blueprint-release.sig'
    subprocess.run(['openssl','dgst','-sha256','-verify',str(root/'public-key.pem'),'-signature',str(signature),str(manifest)],check=True)
    metadata=json.loads(manifest.read_text());version=metadata['Version'];tag='v'+version
    assert version==folder.name and metadata['Product']=='FWBlueprintPlugin' and metadata['PluginId']=='bcb8bf5e-b4ee-45f9-a3ea-bc54de4a7248'
    package=folder/f'FWBlueprintPlugin-{version}-win-x64.zip'
    assert metadata['Package']==f'https://github.com/Frailey-Woodworks/FWBlueprintPlugin-Releases/releases/download/{tag}/{package.name}'
    assert package.stat().st_size==metadata['Bytes'] and hashlib.sha256(package.read_bytes()).hexdigest()==metadata['Sha256']
    with zipfile.ZipFile(package) as archive:
        names=archive.namelist();payload=json.loads(archive.read('payload.json'))
        assert len(names)==len(set(n.lower() for n in names))==len(payload['Files'])+1
        assert payload['Commit']==metadata['Commit'] and payload['Version']==version
        for name,digest in payload['Files'].items():
            assert name in names and '..' not in name.split('/') and not name.startswith('/') and '\\' not in name
            assert name in ('README.txt','THIRD-PARTY-NOTICES.txt','manifest.yml') or re.fullmatch(r'net(?:48|7\.0)/[A-Za-z0-9_.-]+(?:\.dll|\.rhp|\.deps\.json|\.runtimeconfig\.json)',name)
            assert not name.lower().endswith(('.pdb','.cs','.xml'))
            assert hashlib.sha256(archive.read(name)).hexdigest()==digest
    result=subprocess.run(['gh','release','view',tag,'--repo','Frailey-Woodworks/FWBlueprintPlugin-Releases','--json','assets'],capture_output=True,text=True)
    if result.returncode==0:
        assert {a['name'] for a in json.loads(result.stdout)['assets']}=={package.name,manifest.name,signature.name},'Existing release differs; never overwrite'
        continue
    latest=subprocess.run(['gh','release','view','--repo','Frailey-Woodworks/FWBlueprintPlugin-Releases','--json','tagName'],capture_output=True,text=True)
    mark_latest=True
    if latest.returncode==0:
        previous=json.loads(latest.stdout)['tagName'].removeprefix('v')
        mark_latest=tuple(map(int,version.split('.')))>tuple(map(int,previous.split('.')))
    notes='No GitHub account is required. Download and extract the ZIP; drag net7.0/FWBlueprintPlugin.rhp into Rhino 8. Future signed updates stage automatically and load at your next normal restart. Source code remains private. Background update/failure/lifecycle checks passed; native Rhino dialog and restart qualification remain pending the owner\'s Rhino-use release. Open files are never closed by the updater.'
    subprocess.run(['gh','release','create',tag,str(package),str(manifest),str(signature),'--repo','Frailey-Woodworks/FWBlueprintPlugin-Releases','--target','main','--title','Blueprint '+version,'--notes',notes,'--latest='+str(mark_latest).lower()],check=True)
