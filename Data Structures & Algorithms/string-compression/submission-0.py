class Solution:
    def compress(self, chars: List[str]) -> int:

        read = write = 0

        while read < len(chars):

            count = 0
            ch = chars[read]    #for each character comparison

            while read < len(chars) and chars[read] == ch:

                count += 1
                read += 1
            
            chars[write] = ch   #change same grp char
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d   #add digits 
                    write += 1

        return write
