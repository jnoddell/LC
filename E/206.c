/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseList(struct ListNode* head){

    if ( head == NULL ) return head;
    
    struct ListNode* curr = head;
    
    struct ListNode* prev = NULL;
    
    struct ListNode* temp;
    
    while ( curr ) {
        
        temp = curr->next;
        
        curr->next = prev;
        
        prev = curr;
        
        curr = temp;
        
    }
    
    return prev;
    
}
