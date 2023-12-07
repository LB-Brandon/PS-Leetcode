class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # make sorted adjacency list in smallest lexical order
        for ticket in sorted(tickets):
            f, t = ticket
            graph[f].append(t)
        
        def dfs(current):
            # explore all possible destinations
            while graph[current]:
                dfs(graph[current].pop(0))
            # record the decision from the last
            result.append(current)
            
            
        result = []
        dfs("JFK")
        # appending from last decision, so reverse the list
        return result[::-1]
        
        
        
    