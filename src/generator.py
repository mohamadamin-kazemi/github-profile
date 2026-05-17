from pathlib import Path


def generate_profile(theme, **kwargs):
    '''Generate profile readme frome theme and kwargs'''
    # Read theme
    with open(f"src/themes/{theme}/profile.txt", "r") as f:
        profile = f.read()
    # Replace placeholders with user input
    for item, value in kwargs.items():
        item_path = Path(f"src/themes/{theme}/{item}.txt")
        if not item_path.exists():
            continue

        with open(item_path) as f:
            profile_item = f.read()

        profile_item = profile_item.replace(f"{{ value }}", value)
        profile = profile.replace(f"{{ {item} }}", value)   
    return profile

if __name__ == "__main__":
    # Example usage
    name = "John Doe"
    email = "john.doe@example.com"
    location = "New York, USA"
    phone = "+1 234 567 890"
    website = "https://johndoe.com"
    twitter = "john_doe_twitter"
    linkedin = "john_doe_linkedin"
    github = "john_doe_github"
    instagram = "john_doe_instagram"
    theme = "default"
    profile = generate_profile(
        theme=theme,
        name=name,
        email=email,
        website=website,
        twitter=twitter,
        linkedin=linkedin,
        github=github,
        instagram=instagram,
    )
    print(profile)