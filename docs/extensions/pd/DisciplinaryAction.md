---
search:
  boost: 10.0
---

# Class: DisciplinaryAction 


_Information about disciplinary actions and its history_



<div data-search-exclude markdown="1">



URI: [pd:DisciplinaryAction](https://w3id.org/lmodel/dpv/pd/DisciplinaryAction)





```mermaid
 classDiagram
    class DisciplinaryAction
    click DisciplinaryAction href "../DisciplinaryAction/"
      Professional <|-- DisciplinaryAction
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **DisciplinaryAction**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DisciplinaryAction](https://w3id.org/lmodel/dpv/pd/DisciplinaryAction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Disciplinary Action




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DisciplinaryAction |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DisciplinaryAction |
| native | pd:DisciplinaryAction |
| exact | dpv_pd:DisciplinaryAction, dpv_pd_owl:DisciplinaryAction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisciplinaryAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DisciplinaryAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about disciplinary actions and its history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Disciplinary Action
exact_mappings:
- dpv_pd:DisciplinaryAction
- dpv_pd_owl:DisciplinaryAction
is_a: Professional
class_uri: pd:DisciplinaryAction

```
</details>

### Induced

<details>
```yaml
name: DisciplinaryAction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DisciplinaryAction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about disciplinary actions and its history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Disciplinary Action
exact_mappings:
- dpv_pd:DisciplinaryAction
- dpv_pd_owl:DisciplinaryAction
is_a: Professional
class_uri: pd:DisciplinaryAction

```
</details></div>