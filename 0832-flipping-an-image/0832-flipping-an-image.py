class Solution:
    def flipAndInvertImage(self, image):
        
        for i in range(len(image)):
            # Step 1: Flip (reverse) each row
            image[i].reverse()
            
            # Step 2: Invert each element (0 -> 1, 1 -> 0)
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image
