from client import ConversationalCandidateScreeningInterviewAgentClient

def main():
    client = ConversationalCandidateScreeningInterviewAgentClient()
    resume = "Senior AI Engineer with 6 years experience in Python, Kubernetes, and Agentic DAG systems."
    res = client.evaluate_candidate(resume, {"role": "Lead Agent Architect"})
    print(f"Score: {res['competency_score_pct']}%")
    print(f"Recommendation: {res['recommendation']}")
    print(f"Summary: {res['interview_transcript_summary']}")

if __name__ == "__main__":
    main()
