class Solution:
    def braceExpansionII(self, expression):
        
        def parse(i):
            result = {""}
            
            while i < len(expression) and expression[i] != '}':
                
                # Union: current part separated by comma
                if expression[i] == ',':
                    i += 1
                    result |= {""}
                    continue
                
                # Parse a single component
                if expression[i] == '{':
                    part, i = parse(i + 1)
                else:
                    part = {expression[i]}
                    i += 1
                
                # Concatenation
                result = {
                    a + b
                    for a in result
                    for b in part
                }
            
            return result, i + 1 if i < len(expression) and expression[i] == '}' else i

        # The above parser needs union handling slightly differently.
        # Use a cleaner recursive implementation below.
        
        def dfs(i):
            current = {""}
            total = set()

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    total |= current
                    current = {""}
                    i += 1
                    
                elif expression[i] == '{':
                    part, i = dfs(i + 1)
                    current = {
                        a + b
                        for a in current
                        for b in part
                    }
                    
                else:
                    current = {
                        a + expression[i]
                        for a in current
                    }
                    i += 1

            total |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return total, i

        result, _ = dfs(0)
        return sorted(result)