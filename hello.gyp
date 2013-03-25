{

   'includes': [ 'vars.gypi' ],

    'targets': [
      {
        'target_name': 'h1',
         'type': 'executable',
          # 'type': 'static_library',
          'sources': [
                'src/h1.cpp',
          ],

          'cflags': [
            '-Wno-write-strings',
          ],

          'defines': [
               'DEF_1',
               'GYP_VAR_1=<(GYP_VAR_1)', 
           ],

          'include_dirs': [
              '.',
           ],

          'link_settings': {
               'libraries': [
                  '-lc',
                ],
           },

          'actions': [
             {
               'action_name': 'greet',
               'action': [ 'echo', 'hello world <(GYP_VAR_1)', ],
               'inputs': [],
               'outputs': ['yo.c'],

              },
           ],
       }
    ]
}
