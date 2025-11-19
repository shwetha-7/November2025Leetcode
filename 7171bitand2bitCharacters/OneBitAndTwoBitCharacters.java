class OneBitAndTwoBitCharacters{
    private class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int index=0;
        while(index<bits.length){
            if(bits[index]==1) index+=2;
            else index++;
        }
        return index!=bits.length;
    }
}
}