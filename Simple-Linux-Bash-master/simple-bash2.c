#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <pthread.h>

int counter = 0;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

char *prompt="myshell> ";

/*--------Function used to count each occurrence in the thread--------*/
void *counterFunction(char *input, char *searchfile)
{
  int c;
  FILE *file;
  /*---Beginning of the mutex used to protect the critical section----*/
  pthread_mutex_lock(&mutex1);
  file = fopen(searchfile, "r");
  if (file){
    while((c = getc(file)) != EOF){
      if(*input == c){
        counter++;
      }
    }
    fclose(file);
    pthread_mutex_unlock(&mutex1);
  /*---End of the mutex used to protect the critical section----*/
  } else {
    printf("%s could not be found. Moving on to next file.\n", searchfile);
  }
}

main()
{
  int pid;
  int child_pid;
  char line[81];
  char *token;
  char *separator = " \t\n";
  char **args;
  char **cmd1;
  char **cmd2;
  int i;
  int newstdin;
  int newstdout;
  int has_pipe = 0;

    /* max 80 tokens in line */
    args=(char **) malloc(80*sizeof(char *));
    cmd1=(char **) malloc(80*sizeof(char *));
    cmd2=(char **) malloc(80*sizeof(char *));

    fprintf(stderr,"%s",prompt);
    while ( fgets(line,80,stdin) != NULL ) {

   /* get the first token */
   token = strtok(line, separator);
   i=0;
   args[i++]=token;  /* build command array */

   while( token != NULL ) /* walk through other tokens */
   {
      //printf( " %s\n", token );
      token = strtok(NULL, separator);
      args[i++]=token;   /* and build command array */
   }
   args[i]=(char *) NULL;
   /*------Beginning of the piping functionality------*/
   int i = 0;
   int j = 0;
   int count = 0;
   while (args[i] != NULL){
     count++;
     //Checks to see if a pipe is present
     if (!strcmp(args[i], "|")){
       has_pipe = 1;
       break;
     } else {
       token = args[i];
       cmd1[i] = token;
    }
     i++;
   }
   //Breaks the arg vector into two seperate vectors for piping
   if (has_pipe == 1){
     while(args[count] != NULL){
       cmd2[j] = args[count];
       count++;
     }

     /*------Begins creating new process to handle pipe------*/
     int fd[2];
     int status;

	   pipe(fd);

	   switch (pid = fork()) {

  	 case 0: /* child */
  		runpipe(fd, cmd1, cmd2);
  		exit(0);

  	 default: /* parent */
  		 while ((pid = wait(&status)) != -1)
  			 fprintf(stderr, "process %d exits with %d\n", pid, WEXITSTATUS(status));
  	 break;

  	 case -1:
  		 perror("fork");
  		 exit(1);
  	 }
     exit(0);
     /*----End of piping functionality----*/
  }
    /* got all tokes in the argument vector ready to fork */
    /* Begnning of change directory functionality */
    if(!strcmp(args[0], "cd")){
      int dir = 0;
      if (args[1] == NULL){
        chdir("/home");
      } else {
        if(chdir(args[1])){
          fprintf(stderr, "ERROR path: %s does not exist\n", args[1]);
        }
      }
      fprintf(stderr,"%s",prompt);
      continue;
    }
    else if(!strcmp(args[0], "exit")){
      printf("Goodbye :)\n");
      exit(0);
      /* Beginning of "mycount" functionality */
    } else if(!strcmp(args[0], "mycount")){
      int a = 2;
      if(args[1] == NULL){
        printf("Please input a character to search\n");
        fprintf(stderr,"%s",prompt);
        continue;
      } else {
        int filecount = 0;
        //count how many files are being searched through
        while(args[a] != NULL){
          filecount++;
          a++;
        }
        a = 2;
        //initialize threads
        pthread_t thread_id[filecount];
        int j, K, threadcount;
        while (args[a] != NULL) {
          //create thread using the counter function
          pthread_create(&thread_id[i], NULL, counterFunction(args[1], args[a]), NULL);
          threadcount++;
          a++;
        }
        // Join the opened threads
        for(j = 0; j < filecount; j++){
          pthread_join(thread_id[j], NULL);
        }
        printf("%d occurrences of %s found in %d threads. \n", counter, args[1], threadcount);
      }
      fprintf(stderr,"%s",prompt);
      continue;
    }

    switch(pid=fork())
    {
      case 0:  if(args[2] != NULL){       /* child */
                //printf("made it here\n");
                if(!strcmp(args[2], ">")){
                  //printf("Found > \n");
                  if ((newstdout = open(args[3], O_WRONLY | O_TRUNC | O_CREAT, S_IRUSR | S_IRGRP | S_IWGRP | S_IWUSR, 0644)) < 0) {
                    perror(args[3]);	/* open failed */
                    exit(1);
                  }
                  fflush(stdout);
                  dup2(newstdout, 1);
                  args[2] = NULL;
                  args[3] = NULL;
                  close(newstdout);
                } else if(!strcmp(args[2], "<")){
                  //printf("Found < \n");
                    if ((newstdin = open(args[3], O_RDONLY, 0644)) < 0) {
                      perror(args[3]);	/* open failed */
                      exit(1);
                    }
                    dup2(newstdin, 0);
                    args[2] = NULL;
                    args[3] = NULL;
                    close(newstdin);
               } else if(!strcmp(args[2], ">>")){
                     printf("Found >> \n");
                       if ((newstdout = open(args[3], O_WRONLY | O_APPEND, 0644)) < 0) {
                         perror(args[3]);	/* open failed */
                         exit(1);
                       }
                       dup2(newstdout,1);
                       args[2] = NULL;
                       args[3] = NULL;
                       close(newstdout);
                  }
               }
               execvp(args[0],args);
               fprintf(stderr,"ERROR %s no such program\n",line);
               exit(1);
               break;
      case -1: fprintf(stderr,"ERROR can't create child process!\n");   /* unlikely but possible if hit a limit */
               break;
      default: wait();   /* too simple to only do 1 wait - not correct */
     }

    fprintf(stderr,"%s",prompt);
    }
    exit(0);
} /* end main */

void runpipe(int pfd[], char **args1, char **args2)
{
	int pid;

	switch (pid = fork()) {

	case 0: /* child */
		dup2(pfd[0], 0);
		close(pfd[1]);	/* the child does not need this end of the pipe */
		execvp(args2[0], args2);
		perror(args2[0]);

	default: /* parent */
		dup2(pfd[1], 1);
		close(pfd[0]);	/* the parent does not need this end of the pipe */
		execvp(args1[0], args1);
		perror(args1[0]);

	case -1:
		perror("fork");
		exit(1);
	}
}
