import hashlib,json,os,pathlib,re,subprocess,zipfile
# Publishes one signed FW Version Manager bundle (manager/X.Y.Z/) as a GitHub PRE-release with
# tag manager-vX.Y.Z. It is never marked Latest, so the Toolkit's updaters - which read
# /releases/latest and accept only vX.Y.Z tags - are unaffected. Existing releases are never changed.
root=pathlib.Path(__file__).resolve().parents[2]
assert os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')=='Frailey-Woodworks/FWBlueprintPlugin-Releases','Repository-scoped Actions publication only'
repo='Frailey-Woodworks/FWBlueprintPlugin-Releases'
changed=subprocess.check_output(['git','diff-tree','--root','--no-commit-id','--name-only','-r','HEAD'],text=True).splitlines()
folders=sorted({root/pathlib.PurePosixPath(p).parent for p in changed if re.fullmatch(r'manager/\d+\.\d+\.\d+/fw-version-manager-release\.json',p)})
assert len(folders)==1,'Publish one explicitly selected Version Manager release per commit'
for folder in folders:
    manifest=folder/'fw-version-manager-release.json';signature=folder/'fw-version-manager-release.sig';request=json.loads((folder/'publication.json').read_text())
    subprocess.run(['openssl','dgst','-sha256','-verify',str(root/'public-key.pem'),'-signature',str(signature),str(manifest)],check=True)
    m=json.loads(manifest.read_text());v=m['Version'];tag='manager-v'+v
    assert v==folder.name and re.fullmatch(r'\d+\.\d+\.\d+',v)
    assert m['Format']==1 and m['Product']=='FWVersionManager' and m['PluginId']=='78de38af-c927-4bd0-a206-31e1b37a3d76'
    assert request['prerelease'] is True and request['make_latest']=='false' and request['version']==v
    assert request['title']=='FW Version Manager '+v and request['commit']==m['Commit'] and re.fullmatch(r'[0-9a-f]{40}',m['Commit'])
    package=folder/f'fw-version-manager-{v}-win-x64.zip'
    assert m['Package']==f'https://github.com/{repo}/releases/download/{tag}/{package.name}'
    assert package.stat().st_size==m['Bytes'] and hashlib.sha256(package.read_bytes()).hexdigest()==m['Sha256']
    with zipfile.ZipFile(package) as z:
        names=z.namelist();p=json.loads(z.read('payload.json'))
        assert len(names)==len(set(n.lower() for n in names))==len(p['Files'])+1
        assert p['Commit']==m['Commit'] and p['Version']==v and p['Product']==m['Product'] and p['PluginId']==m['PluginId']
        assert set(p['Files'])=={'README.txt','net48/FWVersionManager.rhp','net7.0/FWVersionManager.rhp'},'One self-contained assembly per runtime only'
        for name,digest in p['Files'].items():
            assert hashlib.sha256(z.read(name)).hexdigest()==digest
    before=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/latest']))['tag_name']
    existing=subprocess.run(['gh','api',f'repos/{repo}/releases/tags/{tag}'],capture_output=True,text=True)
    assert existing.returncode!=0 and '404' in existing.stderr,'Release exists or lookup failed; never overwrite'
    subprocess.run(['gh','release','create',tag,str(package),str(manifest),str(signature),'--repo',repo,'--target',os.environ['GITHUB_SHA'],'--title',request['title'],'--notes-file',str(folder/'notes.md'),'--prerelease','--latest=false'],check=True)
    actual=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/tags/{tag}']))
    assert actual['prerelease'] is True and actual['draft'] is False and actual['name']==request['title']
    assert {a['name'] for a in actual['assets']}=={package.name,manifest.name,signature.name}
    after=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/releases/latest']))['tag_name']
    assert before==after,'Latest stable changed'
    print(json.dumps({'version':v,'tag':tag,'prerelease':True,'stableUnchanged':after,'url':actual['html_url']}))
