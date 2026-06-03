---
search:
  boost: 10.0
---

# Class: Education 


_Information about education_



<div data-search-exclude markdown="1">



URI: [pd:Education](https://w3id.org/lmodel/dpv/pd/Education)





```mermaid
 classDiagram
    class Education
    click Education href "../Education/"
      Professional <|-- Education
        click Professional href "../Professional/"
      

      Education <|-- EducationExperience
        click EducationExperience href "../EducationExperience/"
      Education <|-- EducationQualification
        click EducationQualification href "../EducationQualification/"
      Education <|-- EducationTraining
        click EducationTraining href "../EducationTraining/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **Education**
            * [EducationExperience](EducationExperience.md)
            * [EducationQualification](EducationQualification.md)
            * [EducationTraining](EducationTraining.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Education](https://w3id.org/lmodel/dpv/pd/Education) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Education




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Education |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Education |
| native | pd:Education |
| exact | dpv_pd:Education, dpv_pd_owl:Education |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Education
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Education
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about education
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education
exact_mappings:
- dpv_pd:Education
- dpv_pd_owl:Education
is_a: Professional
class_uri: pd:Education

```
</details>

### Induced

<details>
```yaml
name: Education
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Education
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about education
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education
exact_mappings:
- dpv_pd:Education
- dpv_pd_owl:Education
is_a: Professional
class_uri: pd:Education

```
</details></div>