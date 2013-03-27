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
              '<(hrb_common)/expropt2.c',
              '<(hrb_common)/funcid.c',
              '<(hrb_common)/hbarch.c',
              '<(hrb_common)/hbdate.c',
              '<(hrb_common)/hbffind.c',
              '<(hrb_common)/hbfopen.c',
              '<(hrb_common)/hbfsapi.c',
              '<(hrb_common)/hbgete.c',
              '<(hrb_common)/hbhash.c',
              '<(hrb_common)/hbmem.c',
              '<(hrb_common)/hbprintf.c',
              '<(hrb_common)/hbstrbm.c',
              '<(hrb_common)/hbstr.c',
              '<(hrb_common)/hbtrace.c',
              '<(hrb_common)/hbver.c',
              '<(hrb_common)/hbverdsp.c',
              '<(hrb_common)/hbwin.c',
              '<(hrb_common)/hbwince.c',
              '<(hrb_common)/strwild.c'
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
