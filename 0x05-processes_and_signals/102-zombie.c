#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run infinite while loop
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
 * main - Creates five zombie process
 *
 * Return: 0
 */
int main(void)
{
	pid_t pd;
	char cnt = 0;

	while (cnt < 5)
	{
		pd = fork();
		if (pd > 0)
		{
			printf("Zombie process created, PID: %d\n", pd);
			sleep(1);
			cnt++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
