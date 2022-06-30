#include<iostream>
#include <bits/stdc++.h>
using namespace std;
struct Node
{
	int value;
	Node* next;
};

Node* top;
void push(int value)
{
	Node* temp = new Node();
    if (!temp)
	{
		cout << "\n Overflow";
		exit(1);
	}

	temp->value = value;


	temp->next = top;

	top = temp;
}


int empty()
{

	return top == NULL;
}

int peek()
{
	if (!empty())
		return top->value;
	else
		exit(1);
}void pop()
{
	Node* temp;

	if (top == NULL)
	{
		cout << "\n Underflow" << endl;
		exit(1);
	}
	else
	{
		temp = top;
		top = top->next;
        free(temp);
	}
}
void display()
{
	Node* temp;
    if (top == NULL)
	{
		cout << "\n Underflow";
		exit(1);
	}
	else
	{
		temp = top;
		while (temp != NULL)
		{
           cout << temp->value << "-> ";

			temp = temp->next;
		}
	}
}


int main()
{
	push(10);
	push(12);
	push(14);
	push(16);

	display();
cout << "\n1st  element is "
		<< peek() << endl;


	pop();
	pop();

	display();


	cout << "\n1st element is "
		<< peek() << endl;

	return 0;
}
