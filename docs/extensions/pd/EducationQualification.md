---
search:
  boost: 10.0
---

# Class: EducationQualification 


_Information about educational qualifications_



<div data-search-exclude markdown="1">



URI: [pd:EducationQualification](https://w3id.org/lmodel/dpv/pd/EducationQualification)





```mermaid
 classDiagram
    class EducationQualification
    click EducationQualification href "../EducationQualification/"
      Education <|-- EducationQualification
        click Education href "../Education/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * [Education](Education.md)
            * **EducationQualification**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EducationQualification](https://w3id.org/lmodel/dpv/pd/EducationQualification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Education Qualification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EducationQualification |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EducationQualification |
| native | pd:EducationQualification |
| exact | dpv_pd:EducationQualification, dpv_pd_owl:EducationQualification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EducationQualification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationQualification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about educational qualifications
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Qualification
exact_mappings:
- dpv_pd:EducationQualification
- dpv_pd_owl:EducationQualification
is_a: Education
class_uri: pd:EducationQualification

```
</details>

### Induced

<details>
```yaml
name: EducationQualification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationQualification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about educational qualifications
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Qualification
exact_mappings:
- dpv_pd:EducationQualification
- dpv_pd_owl:EducationQualification
is_a: Education
class_uri: pd:EducationQualification

```
</details></div>