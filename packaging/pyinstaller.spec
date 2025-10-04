# PyInstaller configuration file for packaging the AI desktop application

block_cipher = None

a = Analysis(['../src/main.py'],
             pathex=['../src', '../packaging'],
             binaries=[],
             datas=[('../src/models', 'models'), 
                    ('../src/pipelines', 'pipelines'), 
                    ('../src/utils', 'utils'), 
                    ('../src/config', 'config')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
           cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ai_desktop_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ai_desktop_app')