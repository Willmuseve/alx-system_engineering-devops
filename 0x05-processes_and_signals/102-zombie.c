#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * A program that returns five zombie processes
 * for every zombie process created, it displays Zombie process created, PID: ZPMBIE_PID
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
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t z;

	for (i = 0; i < 5; i++)
	{
		z = fork();
		if (!z)
			return (0);
		printf("Zombie process created, PID: %d\n", z);
	}

	infinite_while();
	return (0);
}