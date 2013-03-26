{
    'includes': [ 'vars.gypi' ],

    'variables': {
       'hrb_common' : '<(hrb_root)/src/common',
       'hrb_include' : '<(hrb_root)/include',
    },

    'targets': [
      {

        'target_name': 'hrb_common',
          'type': 'static_library',
          'sources': [
              '<(hrb_common)/expropt1.c',
              '<(hrb_common)/expropt2.c'
          ],

          'cflags': [
            '-Wno-write-strings',
          ],

          'defines': [
               'DEF_1',
               'GYP_VAR_1=<(GYP_VAR_1)', 
           ],

          'include_dirs': [
              '<(hrb_include)',
           ],

          'link_settings': {
               'libraries': [
                  '-lc',
                ],
           },

          'actions': [
             {
               'action_name': 'greet',
               'action': [ 'echo', 'harbour root <(hrb_root)', ],
               'inputs': [],
               'outputs': ['yo.c'],

              },
           ],
       }
    ]
}
