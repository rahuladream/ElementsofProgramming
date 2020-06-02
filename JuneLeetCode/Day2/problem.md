<p class="has-line-data" data-line-start="0" data-line-end="1">Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.</p>
<p class="has-line-data" data-line-start="2" data-line-end="3">Given linked list – head = [4,5,1,9], which looks like following:</p>
<img src="https://assets.leetcode.com/uploads/2018/12/28/237_example.png">
<p class="has-line-data" data-line-start="8" data-line-end="9">Example 1:</p>
<p class="has-line-data" data-line-start="10" data-line-end="14">Input: head = [4,5,1,9], node = 5<br>
Output: [4,1,9]<br>
Explanation: You are given the second node with value 5, the linked list should become 4 -&gt; 1 -&gt; 9 after calling your function.<br>
Example 2:</p>
<p class="has-line-data" data-line-start="15" data-line-end="18">Input: head = [4,5,1,9], node = 1<br>
Output: [4,5,9]<br>
Explanation: You are given the third node with value 1, the linked list should become 4 -&gt; 5 -&gt; 9 after calling your function.</p>
<p class="has-line-data" data-line-start="20" data-line-end="21">Note:</p>
<p class="has-line-data" data-line-start="22" data-line-end="26">The linked list will have at least two elements.<br>
All of the nodes’ values will be unique.<br>
The given node will not be the tail and it will always be a valid node of the linked list.<br>
Do not return anything from your function.</p>