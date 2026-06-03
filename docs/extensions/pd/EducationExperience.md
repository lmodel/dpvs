---
search:
  boost: 10.0
---

# Class: EducationExperience 


_Information about education experience e.g. attending a university_



<div data-search-exclude markdown="1">



URI: [pd:EducationExperience](https://w3id.org/lmodel/dpv/pd/EducationExperience)





```mermaid
 classDiagram
    class EducationExperience
    click EducationExperience href "../EducationExperience/"
      Education <|-- EducationExperience
        click Education href "../Education/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * [Education](Education.md)
            * **EducationExperience**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EducationExperience](https://w3id.org/lmodel/dpv/pd/EducationExperience) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Education Experience




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EducationExperience |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EducationExperience |
| native | pd:EducationExperience |
| exact | dpv_pd:EducationExperience, dpv_pd_owl:EducationExperience |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EducationExperience
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationExperience
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about education experience e.g. attending a university
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Experience
exact_mappings:
- dpv_pd:EducationExperience
- dpv_pd_owl:EducationExperience
is_a: Education
class_uri: pd:EducationExperience

```
</details>

### Induced

<details>
```yaml
name: EducationExperience
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationExperience
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about education experience e.g. attending a university
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Experience
exact_mappings:
- dpv_pd:EducationExperience
- dpv_pd_owl:EducationExperience
is_a: Education
class_uri: pd:EducationExperience

```
</details></div>