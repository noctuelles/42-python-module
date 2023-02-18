kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    for key in kata:
        print('{0} was created by {1}'.format(key, kata[key]))
