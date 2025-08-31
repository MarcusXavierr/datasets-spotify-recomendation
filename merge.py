import pandas as pd
from pydantic import BaseModel
from pandantic import Pandantic
from typing import Optional

## Insights da análise rápida dos datasets
# Não é possível usar gênero para categorizar, pois só tem no dataset secundario, e só tem 5 generos
# Existe alguns outros datasets que tem dados como o genero.

class MainDataset(BaseModel):
    valence: float
    year: int
    acousticness: float
    artists: str
    danceability: float
    duration_ms: int
    energy: float
    explicit: bool
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: bool
    name: str
    popularity: int
    release_date: int|str # TODO: Talvez eu precise tratar pra transformar os anos em datas YYYY-MM-DD
    speechiness: float
    tempo: float

class SecondaryDataset(BaseModel):
    track_id: str
    artists: Optional[str] = None
    album_name: Optional[str] = None
    track_name: Optional[str] = None
    popularity: int
    duration_ms: int
    explicit: bool
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: bool
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    track_genre: str # Não posso usar porque tem só 5 opções

# track_id,artists,album_name,track_name,popularity,duration_ms,explicit,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,time_signature,track_genre

main_df = pd.read_csv('./spotify-main-dataset/data.csv')
secondary_df = pd.read_csv('./spotify-aux-dataset/dataset.csv')

def convert_secondary_to_main(secondary_row: dict) -> dict:
    """
    Convert a secondary dataset row to main dataset schema
    """
    return {
        'valence': secondary_row['valence'],
        'year': None,  # Not available in secondary dataset
        'acousticness': secondary_row['acousticness'],
        'artists': secondary_row.get('artists', ''),
        'danceability': secondary_row['danceability'],
        'duration_ms': secondary_row['duration_ms'],
        'energy': secondary_row['energy'],
        'explicit': secondary_row['explicit'],
        'id': secondary_row['track_id'],
        'instrumentalness': secondary_row['instrumentalness'],
        'key': secondary_row['key'],
        'liveness': secondary_row['liveness'],
        'loudness': secondary_row['loudness'],
        'mode': secondary_row['mode'],
        'name': secondary_row.get('track_name', ''),
        'popularity': secondary_row['popularity'],
        'release_date': None,  # Not available in secondary dataset
        'speechiness': secondary_row['speechiness'],
        'tempo': secondary_row['tempo']
    }

def merge_datasets(main_df: pd.DataFrame, secondary_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge secondary dataset into main dataset, avoiding duplicates based on ID
    """
    # Create a copy of main_df to avoid modifying the original
    merged_df = main_df.copy()
    
    # Get existing IDs from main dataset
    existing_ids = set(merged_df['id'].values)
    
    # Process each row in secondary dataset
    new_rows = []
    for _, row in secondary_df.iterrows():
        # Check if track_id already exists in main dataset
        if row['track_id'] not in existing_ids:
            # Convert to main dataset schema
            converted_row = convert_secondary_to_main(row.to_dict())
            new_rows.append(converted_row)
            # Add to existing_ids to avoid duplicates within the secondary dataset
            existing_ids.add(row['track_id'])
    
    # Create DataFrame from new rows and append to merged_df
    if new_rows:
        new_df = pd.DataFrame(new_rows)
        merged_df = pd.concat([merged_df, new_df], ignore_index=True)
    
    return merged_df

# Example usage:
# merged_data = merge_datasets(main_df, secondary_df)
# print(f"Original main dataset: {len(main_df)} rows")
# print(f"Secondary dataset: {len(secondary_df)} rows")
# print(f"Merged dataset: {len(merged_data)} rows")
# print(f"New tracks added: {len(merged_data) - len(main_df)}")

