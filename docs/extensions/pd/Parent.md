---
search:
  boost: 10.0
---

# Class: Parent 


_Information about parent(s)_



<div data-search-exclude markdown="1">



URI: [pd:Parent](https://w3id.org/lmodel/dpv/pd/Parent)





```mermaid
 classDiagram
    class Parent
    click Parent href "../Parent/"
      FamilyStructure <|-- Parent
        click FamilyStructure href "../FamilyStructure/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * [FamilyStructure](FamilyStructure.md)
            * **Parent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Parent](https://w3id.org/lmodel/dpv/pd/Parent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Parent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Parent |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Parent |
| native | pd:Parent |
| exact | dpv_pd:Parent, dpv_pd_owl:Parent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Parent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Parent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about parent(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Parent
exact_mappings:
- dpv_pd:Parent
- dpv_pd_owl:Parent
is_a: FamilyStructure
class_uri: pd:Parent

```
</details>

### Induced

<details>
```yaml
name: Parent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Parent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about parent(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Parent
exact_mappings:
- dpv_pd:Parent
- dpv_pd_owl:Parent
is_a: FamilyStructure
class_uri: pd:Parent

```
</details></div>