---
search:
  boost: 10.0
---

# Class: Offspring 


_Information about offspring(s)_



<div data-search-exclude markdown="1">



URI: [pd:Offspring](https://w3id.org/lmodel/dpv/pd/Offspring)





```mermaid
 classDiagram
    class Offspring
    click Offspring href "../Offspring/"
      FamilyStructure <|-- Offspring
        click FamilyStructure href "../FamilyStructure/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * [FamilyStructure](FamilyStructure.md)
            * **Offspring**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Offspring](https://w3id.org/lmodel/dpv/pd/Offspring) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Offspring




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Offspring |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Offspring |
| native | pd:Offspring |
| exact | dpv_pd:Offspring, dpv_pd_owl:Offspring |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Offspring
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Offspring
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about offspring(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Offspring
exact_mappings:
- dpv_pd:Offspring
- dpv_pd_owl:Offspring
is_a: FamilyStructure
class_uri: pd:Offspring

```
</details>

### Induced

<details>
```yaml
name: Offspring
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Offspring
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about offspring(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Offspring
exact_mappings:
- dpv_pd:Offspring
- dpv_pd_owl:Offspring
is_a: FamilyStructure
class_uri: pd:Offspring

```
</details></div>