---
search:
  boost: 10.0
---

# Class: Intention 


_Information about intentions_



<div data-search-exclude markdown="1">



URI: [pd:Intention](https://w3id.org/lmodel/dpv/pd/Intention)





```mermaid
 classDiagram
    class Intention
    click Intention href "../Intention/"
      Preference <|-- Intention
        click Preference href "../Preference/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * **Intention**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Intention](https://w3id.org/lmodel/dpv/pd/Intention) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Intention




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Intention |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Intention |
| native | pd:Intention |
| exact | dpv_pd:Intention, dpv_pd_owl:Intention |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Intention
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Intention
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about intentions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Intention
exact_mappings:
- dpv_pd:Intention
- dpv_pd_owl:Intention
is_a: Preference
class_uri: pd:Intention

```
</details>

### Induced

<details>
```yaml
name: Intention
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Intention
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about intentions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Intention
exact_mappings:
- dpv_pd:Intention
- dpv_pd_owl:Intention
is_a: Preference
class_uri: pd:Intention

```
</details></div>