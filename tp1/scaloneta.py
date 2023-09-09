import sys

class Analysis:
    def __init__(self, si, ai):
        self.si = si # coach analysis duration
        self.ai = ai # helper analysis duration

    def __str__(self):
        return str(self.si) + ", " + str(self.ai)
    
    def __lt__(self, otherAnalysis):
        return(self.ai > otherAnalysis.ai or (self.ai == otherAnalysis.ai and self.si < otherAnalysis.si))
    
    def __eq__(self, otherAnalysis):
        return (self.ai == otherAnalysis.ai and self.si == otherAnalysis.si)

def readAnalysisFile(filename):
    analysis_list = []
    with open(filename, "r") as file:
        for line in file:
            si, ai = line.split(",")
            
            if not si.strip().isdigit() or not ai.strip().isdigit():
                continue 
            
            analysis = Analysis(int(si), int(ai))
            analysis_list.append(analysis)

    return analysis_list


def main():
    if len(sys.argv) < 2:
        print("not enough arguments")
        return
    
    analysis_list = readAnalysisFile(sys.argv[1])


if __name__ == "__main__":
    main()