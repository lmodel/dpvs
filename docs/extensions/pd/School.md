---
search:
  boost: 10.0
---

# Class: School 


_Information about school such as name of school, conduct, or grades_

_obtained_



<div data-search-exclude markdown="1">



URI: [pd:School](https://w3id.org/lmodel/dpv/pd/School)





```mermaid
 classDiagram
    class School
    click School href "../School/"
      Professional <|-- School
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **School**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:School](https://w3id.org/lmodel/dpv/pd/School) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* School




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#School |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:School |
| native | pd:School |
| exact | dpv_pd:School, dpv_pd_owl:School |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: School
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#School
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about school such as name of school, conduct, or grades

  obtained'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- School
exact_mappings:
- dpv_pd:School
- dpv_pd_owl:School
is_a: Professional
class_uri: pd:School

```
</details>

### Induced

<details>
```yaml
name: School
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#School
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about school such as name of school, conduct, or grades

  obtained'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- School
exact_mappings:
- dpv_pd:School
- dpv_pd_owl:School
is_a: Professional
class_uri: pd:School

```
</details></div>