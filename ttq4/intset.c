#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "intset.h"

void intset_create(struct intset **s){
    /*
     * Create an intset, place a pointer to it in *s
     */
    *s = (struct intset *)malloc(sizeof(struct intset));
    (*s)->head = NULL;
}

bool in_set(struct intset *s, int elem){
    /*
     * Checks if elem is in set s
     */
    struct node *cur_elem = s->head;
    while(cur_elem != NULL){
        if(elem == cur_elem->data){
            return true;
        }
        cur_elem = cur_elem->next;
    }
    return false;
}

void intset_add(struct intset *s, int *elems, int num_elems){
    /*
     * Add the elements from array elems to intset s
     */
    //find tail
    struct node* new_node;
    struct node* tail;
    int i = 0;

    if(s->head != NULL){
        tail = s->head;
        while(tail->next != NULL){
            tail = tail->next;
        }
    }else{
        new_node = (struct node*)malloc(sizeof(struct node));
        new_node->data = elems[0];
        new_node->next = NULL;
        s->head = new_node;
        i = 1;
        tail = new_node;
    }

    for(i; i < num_elems; i++){
        if(in_set(s, elems[i])){
            continue;
        }
        new_node = (struct node*)malloc(sizeof(struct node));
        new_node->data = elems[i];
        new_node->next = NULL;
        tail->next = new_node;
        tail = tail->next;
    }
}

int intset_iselem(struct intset *s, int elem){
    /*
     * Return 1 if element elem is in intset s. Otherwise return 0.
     */
    struct node* cur_node = s->head;

    while(cur_node != NULL){
        if(cur_node->data == elem){
            return 1;
        }
        cur_node = cur_node->next;
    }
    return 0;
}

void intset_remove(struct intset *s, int elem){
    /*
     * Remove element elem from s if it is in s
     */
    if(intset_iselem(s, elem) == 1){
        //we know that elem is in s
        //find position
        struct node *pre_elem = s->head;
        struct node *cur_elem = s->head;

        while(cur_elem->data != elem){
            pre_elem = cur_elem;
            cur_elem = cur_elem->next;
        }

        //we are now in the position of the element to remove
        pre_elem->next = cur_elem->next;
        free(cur_elem);
    }
}

void intset_union(struct intset *s1, struct intset *s2, struct intset **s3){
    /*
     * computes the union of set s1 and s2 and places the result in s3
     */
    intset_create(s3);

    struct node* cur_elem = s1->head;
    struct node* new_node;
    struct node* pre_node;
    while(cur_elem != NULL){
        if((*s3)->head == NULL){
            new_node = (struct node*)malloc(sizeof(struct node));
            new_node->data = cur_elem->data;
            new_node->next = NULL;
            (*s3)->head = new_node;
            pre_node = new_node;
            cur_elem = cur_elem->next;
            continue;
        }
        if(intset_iselem(*s3, cur_elem->data) == 0){
            pre_node->next = (struct node *)malloc(sizeof(struct node));
            pre_node->next->data = cur_elem->data;
            pre_node->next->next = NULL;
            pre_node = pre_node->next;
        }

        cur_elem = cur_elem->next;
    }

    cur_elem = s2->head;
    while(cur_elem != NULL){
        if((*s3)->head == NULL){
            new_node = (struct node*)malloc(sizeof(struct node));
            new_node->data = cur_elem->data;
            new_node->next = NULL;
            (*s3)->head = new_node;
            pre_node = new_node;
            cur_elem = cur_elem->next;
            continue;
        }
        if(intset_iselem(*s3, cur_elem->data) == 0){
            pre_node->next = (struct node *)malloc(sizeof(struct node));
            pre_node->next->data = cur_elem->data;
            pre_node->next->next = NULL;
            pre_node = pre_node->next;
        }

        cur_elem = cur_elem->next;
    }
}

void print_set(struct intset *intset){
    struct node *cur_node = intset->head;

    while(cur_node != NULL){
        printf("%d\n", cur_node->data);
        cur_node = cur_node->next;
    }
}

int main(void)
{
    printf("Test code for intset\n");
    struct intset *s1;
    struct intset *s2;
    struct intset *s3;
    intset_create(&s1);
    intset_create(&s2);

    // Add the elements 5, 4, 4, 10, 4 to s1
    int to_addA[5] = {5, 4, 4, 10, 4};
    int to_addB[4] = {2, 2, 3, 4};
    int to_addC[2] = {10, 12};

    intset_add(s1, to_addA, 5); // Add the 5 elements from to_addA to the set s1.
    // Ignore repetitions

    intset_add(s1, to_addC, 2); // Add the 2 elements from to_add
    // Ignore repetitions

    intset_add(s2, to_addB, 3); // Add 2, 2, and 3 to s2. Ignore repetitions.

    intset_union(s1, s2, &s3); // Compute the union of the sets
    // s1 and s2, and put the result in s3
    print_set(s1);
    print_set(s2);
    print_set(s3);

    printf("Is 2 in s1? %d\n", intset_iselem(s1, 2)); // 0
    printf("Is 3 in s2? %d\n", intset_iselem(s2, 3)); // 1
    printf("Is 4 in s3? %d\n", intset_iselem(s3, 4)); // 1

    intset_remove(s1, 4);      // Remove the element 4 for the set
    printf("Is 4 in s1? %d\n", intset_iselem(s1, 4)); // 0

}