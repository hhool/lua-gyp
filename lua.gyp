{
  'targets': [
    {
      'target_name': 'liblua',
      'sources': [
        'src/lapi.c',
        'src/lcode.c',
        'src/ldebug.c',
        'src/ldo.c',
        'src/ldump.c',
        'src/lfunc.c',
        'src/lgc.c',
        'src/llex.c',
        'src/lmem.c',
        'src/lobject.c',
        'src/lopcodes.c',
        'src/lparser.c',
        'src/lstate.c',
        'src/lstring.c',
        'src/ltable.c',
        'src/ltm.c',
        'src/lundump.c',
        'src/lvm.c',
        'src/lzio.c',
        'src/lauxlib.c',
        'src/lbaselib.c',
        'src/ldblib.c',
        'src/liolib.c',
        'src/lmathlib.c',
        'src/loslib.c',
        'src/ltablib.c',
        'src/lstrlib.c',
        'src/loadlib.c',
        'src/linit.c',
      ],
      'include_dirs': [
        '.',
        '<(DEPTH)/third_party/lua/src',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/third_party/lua/src',
        ],
      },
      'conditions': [
        ['OS == "win"', {
          'type': 'shared_library',
          'defines': [
            '_WIN32',
            'LUA_BUILD_AS_DLL',
          ],
        }, {
          'type': 'static_library',
          'defines': [
            'LUA_USE_LINUX',
          ],
        }]
      ]
    },
    {
      'target_name': 'lua',
      'type': 'executable',
      'sources': [
        'src/lua.c'
      ],
      'dependencies': [
        'liblua',
      ],
      'conditions': [
        ['OS == "linux"', {
          'defines': [ 'LUA_USE_DLOPEN'],
          'ldflags': ['-ldl'],
        }]
      ]
    },
    {
      'target_name': 'luac',
      'type': 'executable',
      'sources': [
        'src/luac.c',
        'src/print.c',
      ],
      'dependencies': [
        'liblua',
      ],
    },
  ],
}
