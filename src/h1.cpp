#include <stdio.h>

int main() {
   printf("hello 1\n");
   printf("GYP_VAR_1=%s\n", GYP_VAR_1);

#ifdef DEF_1
   printf("DEF_1 defined\n");
#endif
   return 0;
}
