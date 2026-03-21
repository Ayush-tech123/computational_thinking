Reason

This happens because list(data) creates a shallow copy of the list.
While the outer list is copied, the inner lists is still referenced
from the original list.

Thus, both 'data' and 'update_data' share the same inner lists.
When an element inside an inner list is modified, the change occurs in both variables.