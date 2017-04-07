//critical_example2.c
#include <sys/ipc.h>
#include <sys/sem.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


#include "se207_sems.h"


void print_both(FILE *file, FILE *stream, char *actor, char *text) {
  fprintf(stream, "%s: %s", actor, text);
  fprintf(file, "%s: %s", actor, text);
}

int main(int argc, char argv[]){
const char *her_lines[6];
  her_lines[0] = "Donalbain.";
  her_lines[1] = "A foolish thought, to say a sorry sight.";
  her_lines[2] = "There are two lodged together.";
  her_lines[3] = "Consider it not so deeply.";
  her_lines[4] = "These deeds must not be thought \n After these ways; so, it will make us mad.";
  her_lines[5] = "What do you mean?";

  const char *his_lines[5];
  his_lines[0] = "This is a sorry sight.";
  his_lines[1] = "There's one did laugh in's sleep, and one cried \n 'Murder!' That they did wake each other: I stood and heard them: \n But they did say their prayers, and address'd them \n Again to sleep.";
  his_lines[2] = "One cried 'God bless us!' and 'Amen' the other; \n As they had seen me with these hangman's hands. \n Listening their fear, I could not say 'Amen,' \n When they did say 'God bless us!'";
  his_lines[3] = "But wherefore could not I pronounce 'Amen'? \n I had most need of blessing, and 'Amen' \n Stuck in my throat.";
  his_lines[4] = "Methought I heard a voice cry 'Sleep no more! \n Macbeth does murder sleep', the innocent sleep, \n Sleep that knits up the ravell'd sleeve of care, \n The death of each day's life, sore labour's bath, \n Balm of hurt minds, great nature's second course, \n Chief nourisher in life's feast,";
  int length = sizeof(her_lines) / sizeof(her_lines[0]);
  //Use our source file as the "key"
  int id=se207_semget("critical_example2.c",1);
  int pid=fork();  

  if(pid){
    //P1
    FILE *her_file = fopen("herLines.txt", "w");
    int counter1 = 0;
    while(1){
      se207_wait(id);
      print_both(her_file, stderr, "LADY MACBETH: ", her_lines[counter1]);
      if (counter1 == length) {
        fclose(her_file);
        exit(0);
      }
      counter1 += 1;
      printf("\n");
      se207_signal(id);
    }
  }else{
    //P2
    int counter2 = 0;
    FILE *his_file = fopen("hisLines.txt", "w");
    while(1){
      printf("boop");
      if (counter2 == length) {
        fclose(his_file);
        exit(0);
      }
      se207_wait(id);
      print_both(his_file, stdout, "MACBETH: ", his_lines[counter2]);
      counter2 += 1;
      printf("\n");
      se207_signal(id);
    }
  }
}

