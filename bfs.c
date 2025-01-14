#include <stdio.h>
#include <stdbool.h>

void addEdge(int * tree, int location, int data){
    tree[location] = data;
}

void bfs(int * tree, int size, int target){
    int * queue = malloc(sizeof(int) * size);

    //where to pop out from
    int front = 0;
    //where to insert to
    int rear = 0;

    int* visited = malloc(sizeof(int) * size);

    int head = tree[0];

    bool found = false;
    //start bfs
    while(!found){
        int current = head;

        if(current == target){
            found == true;
        }

    }

}

int main(){
    int size = 9;
    int *tree = (int*)malloc(size * sizeof(int));
    int *head = tree[0];
    return 0;
}