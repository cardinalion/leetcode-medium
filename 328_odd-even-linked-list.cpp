class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        
        if (head == NULL || head->next == NULL || head->next->next == NULL) return head;
        
        ListNode* lastodd = head;
        ListNode* firsteven = head->next;
        ListNode* lasteven = firsteven;
        ListNode* curr = firsteven->next;
        ListNode* tmp;
        
        
        do {
            tmp = curr->next;
            lastodd->next = curr;
            curr->next = firsteven;
            lasteven->next = tmp;
            
            lastodd=curr;
            lasteven=lasteven->next;
            if (lasteven == NULL) return head;
            curr=lasteven->next;
        }
        while (curr!= NULL);
            
        return head;
    }
};
