import re

with open("index.tsx") as f:
    content = f.read()

old = """                               }
                           }
                        });"""

new = """                               }
                               }
                           }
                        });"""

# Because it might match multiple things, let's be more specific

old2 = """                                   });
                               }
                           }
                        });
                    }
                });
            }"""

new2 = """                                   });
                               }
                               }
                           }
                        });
                    }
                });
            }"""

if old2 in content:
    content = content.replace(old2, new2, 1)
    with open("index.tsx", "w") as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found")

