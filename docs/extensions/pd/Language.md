---
search:
  boost: 10.0
---

# Class: Language 


_Information about language and lingual history_



<div data-search-exclude markdown="1">



URI: [pd:Language](https://w3id.org/lmodel/dpv/pd/Language)





```mermaid
 classDiagram
    class Language
    click Language href "../Language/"
      External <|-- Language
        click External href "../External/"
      

      Language <|-- Accent
        click Accent href "../Accent/"
      Language <|-- Dialect
        click Dialect href "../Dialect/"
      

      
```





## Inheritance
* [External](External.md)
    * **Language**
        * [Accent](Accent.md)
        * [Dialect](Dialect.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Language](https://w3id.org/lmodel/dpv/pd/Language) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Language




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Language |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Language |
| native | pd:Language |
| exact | dpv_pd:Language, dpv_pd_owl:Language |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Language
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Language
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about language and lingual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Language
exact_mappings:
- dpv_pd:Language
- dpv_pd_owl:Language
is_a: External
class_uri: pd:Language

```
</details>

### Induced

<details>
```yaml
name: Language
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Language
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about language and lingual history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Language
exact_mappings:
- dpv_pd:Language
- dpv_pd_owl:Language
is_a: External
class_uri: pd:Language

```
</details></div>