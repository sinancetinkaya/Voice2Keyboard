# -*- mode: python -*-

block_cipher = None


a = Analysis(['v2k.py'],
             pathex=['H:\\users\\sinan\\workspace\\v2k'],
             hiddenimports=[],
             hookspath=['pyinstaller-hooks/'],
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='v2k.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='v2k')
