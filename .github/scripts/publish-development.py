import hashlib,json,os,pathlib,re,subprocess,sys,zipfile
root=pathlib.Path(__file__).resolve().parents[2]
assert os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')=='Frailey-Woodworks/FWBlueprintPlugin-Releases','Repository-scoped Actions publication only'
repo='Frailey-Woodworks/FWBlueprintPlugin-Releases'
changed=subprocess.check_output(['git','diff-tree','--root','--no-commit-id','--name-only','-r','HEAD'],text=True).splitlines()
folders=sorted({root/pathlib.PurePosixPath(p).parent for p in changed if re.fullmatch(r'development/1\.88\.(?:[1-9]|[1-9]\d)/blueprint-release.json',p)})
assert len(folders)==1,'Publish one explicitly selected development release per commit'
for folder in folders:
    manifest=folder/'blueprint-release.json';signature=folder/'blueprint-release.sig';request=json.loads((folder/'publication.json').read_text())
    subprocess.run(['openssl','dgst','-sha256','-verify',str(root/'public-key.pem'),'-signature',str(signature),str(manifest)],check=True)
    m=json.loads(manifest.read_text());v=m['Version'];tag='v'+v
    assert v==folder.name and re.fullmatch(r'1\.88\.(?:[1-9]|[1-9]\d)',v)
    assert m['Product']=='FWBlueprintPlugin' and m['PluginId']=='bcb8bf5e-b4ee-45f9-a3ea-bc54de4a7248'
    assert request['prerelease'] is True and request['make_latest']=='false' and request['version']==v
    assert request['title'].startswith('Blueprint '+v+' (dev) - ') and request['commit']==m['Commit']
    package=folder/f'FWBlueprintPlugin-{v}-win-x64.zip'
    assert m['Package']==f'https://github.com/{repo}/releases/download/{tag}/{package.name}'
    assert package.stat().st_size==m['Bytes'] and hashlib.sha256(package.read_bytes()).hexdigest()==m['Sha256']
    with zipfile.ZipFile(package) as z:
        names=z.namelist();p=json.loads(z.read('payload.json'))
        assert len(names)==len(set(n.lower() for n in names))==len(p['Files'])+1
        assert p['Commit']==m['Commit'] and p['Version']==v
        for name,digest in p['Files'].items():
            assert '..' not in name.split('/') and not name.startswith('/') and '\\' not in name
            assert name in ('README.txt','THIRD-PARTY-NOTICES.txt','manifest.yml') or re.fullmatch(r'net(?:48|7\.0)/[A-Za-z0-9_.-]+(?:\.dll|\.rhp|\.deps\.json|\.runtimeconfig\.json)',name)
            assert not name.lower().endswith(('.pdb','.cs','.xml')) and name.split('/')[-1].lower() not in ('rhinocommon.dll','eto.dll')
            assert hashlib.sha256(z.read(name)).hexdigest()==digest
        for runtime in ('net48','net7.0'): assert runtime+'/FWBlueprintPlugin.rhp' in names
    before=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/latest']))['tag_name']
    existing=subprocess.run(['gh','api',f'repos/{repo}/releases/tags/{tag}'],capture_output=True,text=True)
    assert existing.returncode!=0 and '404' in existing.stderr,'Release exists or lookup failed; never overwrite'
    subprocess.run(['gh','release','create',tag,str(package),str(manifest),str(signature),'--repo',repo,'--target',os.environ['GITHUB_SHA'],'--title',request['title'],'--notes-file',str(folder/'notes.md'),'--prerelease','--latest=false'],check=True)
    actual=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/tags/{tag}']))
    assert actual['prerelease'] is True and actual['draft'] is False and actual['name']==request['title']
    assert {a['name'] for a in actual['assets']}=={package.name,manifest.name,signature.name}
    after=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/latest']))['tag_name']
    assert before==after,'Latest stable changed'
    print(json.dumps({'version':v,'prerelease':True,'stableUnchanged':after,'url':actual['html_url']}))
