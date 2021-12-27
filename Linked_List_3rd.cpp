#include <iostream>
using namespace std;

class Node
{
public:
    string name;
    string prn;
    Node *next;
};

Node *head = NULL;
Node *last = NULL;

void display_members()
{
    Node *ptr = head;

    cout << endl << "All members in the Club are" << endl << endl;
    while (ptr != NULL)
    {
        cout << "Name is: " << ptr->name << endl;
        cout << "PRN is: " << ptr->prn << endl << endl;
        ptr = ptr->next;
    }
}

void count_total_members()
{
    Node *ptr = head;
    int count = 0;
    while (ptr != NULL)
    {
        count++;
        ptr = ptr->next;
    }
    cout << "Total Members in the Club are: " << count << endl;
}

void add_member()
{
    string name;
    string prn;
    Node *ptr = head;
    Node  *j = ptr->next;
    Node *new_member = new Node();

    cout << endl << "Enter Name of New Member: " << endl;
    cin >> name;

    cout << "Enter PRN of Member" << endl;
    cin >> prn;

    new_member->name = name;
    new_member->prn = prn;

    while(j != last)
    {
        ptr = ptr->next;
        j = j->next;
    }

    ptr->next = new_member;
    new_member->next = j;
}

void delete_member()
{
    string name;
    Node *delete_member = head;
    Node *prev = NULL;

    cout << endl << "Enter Name of Member to Delete: " << endl;
    cin >> name;

    while(delete_member->name != name && delete_member != last)
    {
        prev = delete_member;
        delete_member = delete_member->next;
    }

    if (delete_member->name == name)
    {
        prev->next = delete_member->next;
        free(delete_member);
        cout << name << " Removed from the Club." << endl << endl;
    }
    else
    {
        cout << "No Member named "<< name << " in Club." << endl << endl;
    }
}

int main()
{
    head = new Node();
    last = new Node();

    head->name = "Vivek Harwani";
    head->prn = "President";
    head->next = last;

    last->name = "Sachin";
    last->prn = "Secretary";
    last->next = NULL;

    display_members();
    count_total_members();
    add_member();
    display_members();
    add_member();
    display_members();
    count_total_members();
    delete_member();
    count_total_members();
    display_members();


}
