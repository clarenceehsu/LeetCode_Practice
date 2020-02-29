'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
'''

#=====================================================================================================#

# First


class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for n in [n for n in path.split('/') if n != '' and n != '.']:
            if n == '..':
                ans = ans[:-1]
            else:
                ans.append(n)

        return '/' + '/'.join(ans)

# 24ms, 12.9MB
# 观察可以发现一个规律，斜杠不管多少都只做分割用，一个点可以忽略，两个点返回上个目录，然后根据这个逻辑编写代码即可

#=====================================================================================================#

# Second


class Solution:
    def simplifyPath(self, path: str) -> str:
        return os.path.abspath(path)

# 24ms, 12.9MB
# 一行怪，真的帅

#=====================================================================================================#