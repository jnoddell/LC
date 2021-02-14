#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

class Solution {
    
public:
    
    int uniqueMorseRepresentations(vector<string>& words) {
        
        string ALPHABET = "abcdefghijklmnopqrstuvwxyz";
        
        string CONVERSION_TABLE[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        vector<string> translations;
        
        for (auto& word : words) {
            
            string translation = "";
            
            for (auto& curr_char : word) {
                
                int index = ALPHABET.find(curr_char);
                
                translation += CONVERSION_TABLE[index];
                
            }
            
            if (find(translations.begin(), translations.end(), translation) != translations.end()) {
                
              // pass
                
            } else {
                    
                translations.push_back(translation);
                
            }
            
        }
        
        return translations.size();
        
    }
    
};
