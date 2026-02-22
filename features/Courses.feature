Feature: Instructor Course Creation Process

  @coursesSteps
  Scenario: Successfully create a new course with all 7 steps

    Given the instructor is logged in with valid credentials
    And the instructor navigates to the new course creation page

    When the instructor completes Step 1: Basic Information
      | title       | description                  |
      | mathematics | This is a mathematics course |

    And the instructor completes Step 2: Extra Information
      | capacity | duration | tags | category |
      | 60       | 90       | test | 956      |

    And the instructor completes Step 3: Pricing
      | price | days |
      | 0     | 15   |

    And the instructor completes Step 4: Creating a Section
      | section_title      |
      | Yeni Bölüm Başlığı |

    And the instructor completes Step 5: Prerequisites
      | search_text |
      | SDET        |

    And the instructor completes Step 6: FAQ
      | question                        | answer                 |
      | Ogretmenler ile gorusme sıklıgı | 2 haftada 1 15 dk zoom |

    Then the instructor completes Step 7: Quiz and Publishes
      | quiz_title            | attempts |
      | Certifica alma sınavı | 3        |
