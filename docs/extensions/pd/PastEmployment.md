---
search:
  boost: 10.0
---

# Class: PastEmployment 


_Information about past employment_



<div data-search-exclude markdown="1">



URI: [pd:PastEmployment](https://w3id.org/lmodel/dpv/pd/PastEmployment)





```mermaid
 classDiagram
    class PastEmployment
    click PastEmployment href "../PastEmployment/"
      EmploymentHistory <|-- PastEmployment
        click EmploymentHistory href "../EmploymentHistory/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * [EmploymentHistory](EmploymentHistory.md)
            * **PastEmployment**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PastEmployment](https://w3id.org/lmodel/dpv/pd/PastEmployment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Past Employment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PastEmployment |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PastEmployment |
| native | pd:PastEmployment |
| exact | dpv_pd:PastEmployment, dpv_pd_owl:PastEmployment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PastEmployment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PastEmployment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about past employment
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Past Employment
exact_mappings:
- dpv_pd:PastEmployment
- dpv_pd_owl:PastEmployment
is_a: EmploymentHistory
class_uri: pd:PastEmployment

```
</details>

### Induced

<details>
```yaml
name: PastEmployment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PastEmployment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about past employment
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Past Employment
exact_mappings:
- dpv_pd:PastEmployment
- dpv_pd_owl:PastEmployment
is_a: EmploymentHistory
class_uri: pd:PastEmployment

```
</details></div>