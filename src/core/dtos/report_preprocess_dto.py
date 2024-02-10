from typing import List, TypedDict

class DropFeaturesDTO(TypedDict):
  summary: str
  description: str
  platform: str
  
class AggregateTextDTO(TypedDict):
  text: str

CleanSentenceDTO = AggregateTextDTO
RemoveStopwordsDTO = AggregateTextDTO
GenerateSentEmbeddingDTO = List[float]




