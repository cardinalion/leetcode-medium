class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode dummy(0);
        int carry = 0;
        ListNode* tmp = &dummy;
        while (l1 || l2){
            if (l1){
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2){
                carry += l2->val;
                l2 = l2->next;
            }
            tmp->next = new ListNode(carry%10);    
            carry = carry < 10 ? 0 : 1;
            tmp = tmp->next;
        }
        
        if (carry == 1) {
            tmp->next = new ListNode(1);
        }
        return dummy.next; 
    }
};
