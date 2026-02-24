<h1>Data Structures &amp; Algorithms Toolkit</h1>

<p>
  This project demonstrates foundational computer science concepts through custom implementations of core data
  structures and algorithms in Python.
</p>

<h2>Features</h2>

<h3>Queue Abstraction</h3>
<ul>
  <li>Implemented an abstract <code>AbstractQueue</code> interface using Python’s <code>ABC</code> module.</li>
  <li>Enforced consistent queue behavior across multiple implementations.</li>
</ul>

<h3>Queue Implementations</h3>

<h4>PythonListQueue</h4>
<ul>
  <li>Array-backed implementation.</li>
  <li><strong>O(1)</strong> enqueue, <strong>O(n)</strong> dequeue due to element shifting.</li>
</ul>

<h4>SLLQueue</h4>
<ul>
  <li>Backed by a custom singly linked list.</li>
  <li><strong>O(1)</strong> enqueue and dequeue operations.</li>
  <li>Maintains head and tail references for efficiency.</li>
</ul>

<h3>Singly Linked List</h3>
<ul>
  <li>Custom <code>SinglyLinkedListNode</code> and <code>SinglyLinkedList</code> classes.</li>
  <li>Supports insertion/removal at both beginning and end.</li>
  <li>Maintains dynamic size tracking.</li>
</ul>

<h3>Sorting Algorithms</h3>
<ul>
  <li><strong>Merge Sort</strong> (stable, <strong>O(n log n)</strong>)</li>
  <li><strong>Quick Sort</strong> (average <strong>O(n log n)</strong>, worst <strong>O(n²)</strong>)</li>
  <li><strong>Pancake Sort</strong> (flip-based sorting technique)</li>
</ul>

<h3>Search Algorithm</h3>
<ul>
  <li><strong>Binary Search</strong> (<strong>O(log n)</strong>) on sorted datasets.</li>
</ul>

<h2>Key Concepts Demonstrated</h2>
<ul>
  <li>Abstraction &amp; Interface Design</li>
  <li>Polymorphism</li>
  <li>Divide-and-Conquer Algorithms</li>
  <li>Time &amp; Space Complexity Analysis</li>
  <li>Data Structure Performance Tradeoffs</li>
</ul>
