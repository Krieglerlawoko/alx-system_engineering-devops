#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t p;
	char c = 0;

	while (c < 5)
	{
		p = fork();
		if (p > 0)
		{
			printf("Zombie process created, PID: %d\n", p);
			sleep(1);
			c++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
