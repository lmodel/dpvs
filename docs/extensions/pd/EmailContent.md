---
search:
  boost: 10.0
---

# Class: EmailContent 


_Information about the contents of emails sent or received_



<div data-search-exclude markdown="1">



URI: [pd:EmailContent](https://w3id.org/lmodel/dpv/pd/EmailContent)





```mermaid
 classDiagram
    class EmailContent
    click EmailContent href "../EmailContent/"
      Communication <|-- EmailContent
        click Communication href "../Communication/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * **EmailContent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EmailContent](https://w3id.org/lmodel/dpv/pd/EmailContent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Email Content




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EmailContent |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EmailContent |
| native | pd:EmailContent |
| exact | dpv_pd:EmailContent, dpv_pd_owl:EmailContent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmailContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the contents of emails sent or received
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Content
exact_mappings:
- dpv_pd:EmailContent
- dpv_pd_owl:EmailContent
is_a: Communication
class_uri: pd:EmailContent

```
</details>

### Induced

<details>
```yaml
name: EmailContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the contents of emails sent or received
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Content
exact_mappings:
- dpv_pd:EmailContent
- dpv_pd_owl:EmailContent
is_a: Communication
class_uri: pd:EmailContent

```
</details></div>