class Solution
{
public:
    Node *reverse(Node *head, int k)
    {
        vector<int>a;

        Node*t=head;

        while(t!=NULL)
        {
            a.emplace_back(t->data);

            t=t->next;
        }
        int i=0,j=k-1;
        while(i<j)
        {
            swap(a[i],a[j]);
            i++;
            j--;
        }
        i=k,j=a.size()-1;
        while(i<j)
        {
            swap(a[i],a[j]);
            i++;
            j--;
        }
        t=head;
        for(int i=0;i<a.size();i++)
        {
            t->data=a[i];
            t=t->next;
        }
        return head;
    }
};
