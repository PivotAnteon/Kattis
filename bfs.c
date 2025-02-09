#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void addEdge(int * tree, int location, int data){
    tree[location] = data;
}

void printTree(int* tree, int size){
    for(int i = 0; i < size; i++){
        printf("%d ", tree[i]);
    }
    printf("\n\n\n\n");

}

void bfs(int *tree, int size, int target) {
    if (tree == NULL || size < 1) {
        printf("No tree available\n");
        return;
    }

    int *queue = malloc(sizeof(int) * size);
    int *visited = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) visited[i] = 0;

    // BFS initialization
    int front = 0, rear = 0;
    queue[rear++] = 0;  // Start with the root node (index 0)
    visited[0] = 1;

    while (front < rear) {
        int currentIndex = queue[front++];
        int currentValue = tree[currentIndex];

        // Check for target
        if (currentValue == target) {
            printf("Found: %d at index %d\n", target, currentIndex);
            free(queue);
            free(visited);
            return;
        }

        // Enqueue left child
        int leftIndex = currentIndex * 2 + 1;
        if (leftIndex < size && !visited[leftIndex]) {
            queue[rear++] = leftIndex;
            visited[leftIndex] = 1;
        }

        // Enqueue right child
        int rightIndex = currentIndex * 2 + 2;
        if (rightIndex < size && !visited[rightIndex]) {
            queue[rear++] = rightIndex;
            visited[rightIndex] = 1;
        }
    }

    printf("Target not found\n");
    free(queue);
    free(visited);
}

int main(){
    int size = 9;
    int *tree = (int*)malloc(size * sizeof(int));

    for(int i = 0; i < size; i++){
        addEdge(tree, i, rand() * 10);
    }

    printTree(tree, size);

    bfs(tree, size, 6);

    return 0;
}