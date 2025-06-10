
def convert_to_basketball(pitching_stats):
    # Validate required stats
    required_stats = [
        'K%', 'Whiff%', 'Fastball Velocity', 'Hard Hit%', 'BB%', 'Extension',
        'GB%', 'Barrel%', 'xBA', 'Avg Exit Velocity', 'xERA', 'Chase%',
        'Breaking Run Value', 'Fastball Run Value', 'Offspeed Run Value',
        'Pitching Run Value'
    ]

    for stat in required_stats:
        if stat not in pitching_stats:
            raise ValueError(f"Missing required stat: {stat}")

    # Calculate each attribute (NO INVERSION NEEDED)
    return [
        # Inside Scoring (avg of Fastball Velocity, Hard Hit%, Fastball Run Value)
        round((
            pitching_stats['Fastball Velocity'] +
            pitching_stats['Hard Hit%'] +
            pitching_stats['Fastball Run Value']
        ) / 3),

        # Mid Range (avg of Whiff% and Breaking Run Value)
        round((
            pitching_stats['Whiff%'] +
            pitching_stats['Breaking Run Value']
        ) / 2),

        # 3P Shooting (directly maps to K%)
        round(pitching_stats['K%']),

        # Handling (directly maps to BB% control)
        round(pitching_stats['BB%']),

        # Passing (avg of Extension and Offspeed Run Value)
        round((
            pitching_stats['Extension'] +
            pitching_stats['Offspeed Run Value']
        ) / 2),

        # Rebounding (directly maps to GB%)
        round(pitching_stats['GB%']),

        # Post Defense (avg of Avg Exit Velocity and xERA)
        round((
            pitching_stats['Avg Exit Velocity'] +
            pitching_stats['xERA']
        ) / 2),

        # Perimeter Defense (avg of Barrel% and xBA)
        round((
            pitching_stats['Barrel%'] +
            pitching_stats['xBA']
        ) / 2),

        # Stealing (directly maps to Chase%)
        round(pitching_stats['Chase%']),

        # Shot Blocking (avg of Avg Exit Velocity and Extension)
        round((
            pitching_stats['Avg Exit Velocity'] +
            pitching_stats['Extension']
        ) / 2),

        # Physical Attributes (avg of Fastball Velocity, Extension, Pitching Run Value)
        round((
            pitching_stats['Fastball Velocity'] +
            pitching_stats['Extension'] +
            pitching_stats['Pitching Run Value']
        ) / 3)
    ]

# Example usage with "higher = better" percentiles
sample_input = {
    'Pitching Run Value': 105,
    'Fastball Run Value': 99,
    'Breaking Run Value': 83,
    'Offspeed Run Value': 105,
    'xERA': 81,
    'xBA': 72,
    'Fastball Velocity': 86,
    'Avg Exit Velocity': 98,
    'Chase%': 70,
    'Whiff%': 68,
    'K%': 92,
    'BB%': 49,
    'Barrel%': 77,
    'Hard Hit%': 95,
    'GB%': 68,
    'Extension': 71
}

output = convert_to_basketball(sample_input)
attribute_names = [
    "Inside Scoring", "Mid Range", "3P Shooting", "Handling", "Passing",
    "Rebounding", "Post Defense", "Perimeter Defense", "Stealing",
    "Shot Blocking", "Physical Attributes"
]

for name, value in zip(attribute_names, output):
    print(f"{name}: {value}")