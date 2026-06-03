---
search:
  boost: 10.0
---

# Class: Accent 


_Information about linguistic and speech accents_



<div data-search-exclude markdown="1">



URI: [pd:Accent](https://w3id.org/lmodel/dpv/pd/Accent)





```mermaid
 classDiagram
    class Accent
    click Accent href "../Accent/"
      Language <|-- Accent
        click Language href "../Language/"
      
      
```





## Inheritance
* [External](External.md)
    * [Language](Language.md)
        * **Accent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Accent](https://w3id.org/lmodel/dpv/pd/Accent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Accent




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Accent |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Accent |
| native | pd:Accent |
| exact | dpv_pd:Accent, dpv_pd_owl:Accent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Accent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Accent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about linguistic and speech accents
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Accent
exact_mappings:
- dpv_pd:Accent
- dpv_pd_owl:Accent
is_a: Language
class_uri: pd:Accent

```
</details>

### Induced

<details>
```yaml
name: Accent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Accent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about linguistic and speech accents
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Accent
exact_mappings:
- dpv_pd:Accent
- dpv_pd_owl:Accent
is_a: Language
class_uri: pd:Accent

```
</details></div>